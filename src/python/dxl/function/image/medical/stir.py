def render_recon_spec(spec) -> str:
    pass


from dxl.data import Pair, NumPair, Table, NamedTuple
import numpy as np


class Event(NamedTuple):
    __slot__ = ['id_ring', 'id_crystal']


LoR = Pair[Event]


from typing import List


LoRs = Table[LoR]


def listmode2sinogram(scanner, listmode_data: Table[LoR]) -> 'Sinogram':
    # listmode_data array of [7, None]

    return accumulating2sinogram(scanner, listmode_data.fmap(rework_indices))


def fix_crystal_id(scanner, index):
    return (index + scanner.nb_detectors // 4) % scanner.nb_detectors


def center_of_crystal(crystal_id, nb_detectors):
    x = np.sin((0.5 + crystal_id)) * (2 * np.pi) / nb_detectors
    y = np.cos((0.5 + crystal_id)) * (2 * np.pi) / nb_detectors
    return (x, y)


def find_rind_index(lor, nb_detectors):
    crystal_centers = lor.fmap2(
        lambda e: center_of_crystal(e.id_crystal, nb_detectors))

    def is_need_swap_rind_id_and_preseve_crystal_id(centers):
        if centers.fst[0] > centers.snd[0]:
            return True
        if centers.fst[0] == centers.snd[0] and centers.fst[1] < centers.snd[1]:
            return True
        return False

    def is_need_swap_crystal_id_and_preseve_rind_id(centers):
        if centers.fst[0] < centers.snd[0]:
            return True
        if centers.fst[0] == centers.snd[0] and centers.fst[1] > centers.snd[1]:
            return True
        return False
    if is_need_swap_crystal_id_and_preseve_rind_id(crystal_centers):
        return LoR(Event(lor.snd.id_ring, lor.fst.id_crystal),
                   Event(lor.fst.id_ring, lor.snd.id_crystal))
    if is_need_swap_rind_id_and_preseve_crystal_id(center_of_crystal):
        return LoR(Event(lor.fst.id_ring, lor.snd.id_crystal),
                   Event(lor.snd.id_ring, lor.fst.id_crystal))
    return lor


def rework_indices(scanner, lor: Pair[Event]):
    return find_rind_index(lor.fmap2(lambda e: e.replace(id_crystal=fix_crystal_id(scanner, e.id_crystal))),
                           scanner.nb_detectors)


def accumulating2sinogram(scanner, lors: List[LoR]):
    nb_radial_elem = scanner.nb_detectors // 2
    nb_sinograms = scanner.nb_rings * scanner.nb_rings
    result = np.zeros([nb_radial_elem, nb_radial_elem, nb_sinograms])
    for lor in lors:
        ids_ring = lors.fmap2(lambda e: e.id_ring)
        delta_z = ids_ring.snd - ids_ring.fst
        id_sinogram = (ids_ring.fst + ids_ring.snd - abs(delta_z)) // 2 + \
            (scanner.nb_ring if delta_z != 0 else 0)
        for i in range(1, abs(delta_z)):
            id_sinogram += 2 * (scanner.nb_rings - i)
        if(delta_z < 0):
            id_sinogram += scanner.nb_ring - abs(delta_z)

        id_view = (int(sum(ids_ring) + scanner.nb_detectors //
                       2 + 1) / 2) % scanner.nb_detectors // 2

        def diff(id_):
            return min(abs(id_ - id_view), abs(id_ - (id_view + scanner.nb_detectors)))
        diffs = ids_ring.fmap(diff)
        if (abs(diffs.fst) < abs(diffs.snd)):
            sigma = ids_ring.fst - ids_ring.snd
        else:
            sigma = ids_ring.snd - ids_ring.fst

        if (sigma < 0):
            sigma += scanner.nb_detectors
        id_bin = sigma + (nb_radial_elem) / 2 - scanner.nb_detectors / 2
        if id_bin > 0 and id_bin < nb_radial_elem:
            result[id_sinogram, id_bin, id_view] += 1
    return result.reshape([-1, 1])
