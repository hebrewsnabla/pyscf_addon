from pyscf import gto, scf
from pyphf import guess

mol = gto.Mole()
mol.atom = '''H 0.0 0.0 0.0; H 0.0 0.0 2.0'''
mol.basis = '3-21g'
mol.build()

mf = scf.RHF(mol)
mf.max_cycle = 5
mf.kernel()

dm_mix = guess.init_guess_mixed(mf.mo_coeff, mf.mo_occ)
mf_mix = scf.UHF(mol)
mf_mix.kernel(dm0 = dm_mix)

print(mf_mix.mo_coeff)

mf2 = mf_mix
scf.chkfile.dump_scf(mf2.mol, 'test.chk', mf2.e_tot, mf2.mo_energy, mf2.mo_coeff, mf2.mo_occ)


print(mf2.mo_coeff)
