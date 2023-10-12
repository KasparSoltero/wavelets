import wavelets as wl

lpf_D, hpf_D, lpf_R, hpf_R = wl.getFilters("db1")
ca, cd = wl.dwt([0,1,1,1], lpf_D, hpf_D)
print(ca)
print(cd)
print(wl.idwt(ca, cd, 4, lpf_R, hpf_R))
