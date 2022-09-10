Teori = float(input('Nilai Ujian Teori : '))
Praktek = float(input('Nilai Ujian Praktek : '))
if Teori >= 70 and Praktek >= 70 :
    print("Selamat, anda lulus! ")
elif Teori >= 70 and Praktek < 70 :
    print('Anda harus mengulang ujian praktek.')
elif Teori < 70 and Praktek >= 70 :
    print('Anda harus mengulang ujian teori.')
else :
    print('Anda harus mengulang ujian teori dan praktek.')