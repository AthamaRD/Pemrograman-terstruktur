print("***Status Kelulusan Mahasiswa***")
NAMA= (input("Nama : "))
MATH= int(input("Nilai Matematika : "))
BINDO= int(input("Nilai Bahasa Indonesia :"))
IPA= int(input("Nilai IPA :"))
if(MATH<0) or (BINDO<0) or (IPA<60) or (MATH>100) or (BINDO>100) or (IPA>100):
    print("Maaf input anda tidak sesuai atau valid")
elif(MATH>70) and (BINDO>60) and (IPA>60):
    print("Hasil Kelulusan : ", NAMA,"DINYATAKAN LULUS")
else:
    print("Hasil Kelulusan : ", NAMA,"DINYATAKAN TIDAK LULUS")
    print("SEBAB")
    if(MATH<70):
        print("Nilai Matematika kamu kurang dari 70")
    if(BINDO<60):
        print("Nilai Bahasa Indonesia kamu kurang dari 60")
    if(IPA<60):
        print("Nilai IPA kurang dari 60")