# =========================
# utils.py
# Modul konversi suhu
# =========================

def konversi_suhu(nilai, dari, ke):
    """Mengonversi suhu dari satu satuan ke satuan lain (C, F, K)."""

    # ubah input ke huruf kecil
    dari = dari.lower()
    ke = ke.lower()

    # validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "❌ Error: satuan harus 'C', 'F', atau 'K'."

    # validasi nilai suhu Kelvin
    if dari == "k" and nilai < 0:
        return "❌ Error: suhu Kelvin tidak boleh negatif."

    # konversi ke Celsius dulu
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        c = nilai - 273.15

    # dari Celsius ke satuan tujuan
    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9/5) + 32
    elif ke == "k":
        return c + 273.15
