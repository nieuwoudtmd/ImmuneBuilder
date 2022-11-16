import os
from ImmuneBuilder import ABodyBuilder2
from ImmuneBuilder.refine import refine

predictor = ABodyBuilder2()

filename = "3SE8_r_ab2.pdb"
dirname = "3SE8"
os.makedirs(dirname, exist_ok = True)

sequences = {
  'H': 'QVQLVQSGAVIKTPGSSVKISCRASGYNFRDYSIHWVRLIPDKGFEWIGWIKPLWGAVSYARQLQGRVSMTRQLSQDPDDPDWGVAYMEFSGLTPADTAEYFCVRRGSCDYCGDFPWQYWCQGTVVVVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSC',
  'L': 'EIVLTQSPGILSLSPGETATLFCKASQGGNAMTWYQKRRGQVPRLLIYDTSRRASGVPDRFVGSGSGTDFFLTINKLDREDFAVYYCQQFEFFGLGSELEVHRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC'}

# antibody = predictor.predict(sequences)
# antibody.save_all(dirname=dirname, filename=filename)

# refine other models
filename_new = filename.split(".")[0] + "_rank2"
final_filename = os.path.join(dirname, filename_new)
refine(os.path.join(dirname,"rank1_unrefined.pdb"), final_filename)

filename_new = filename.split(".")[0] + "_rank3"
final_filename = os.path.join(dirname, filename_new)
refine(os.path.join(dirname,"rank2_unrefined.pdb"), final_filename)

filename_new = filename.split(".")[0] + "_rank4"
final_filename = os.path.join(dirname, filename_new)
refine(os.path.join(dirname,"rank3_unrefined.pdb"), final_filename)
