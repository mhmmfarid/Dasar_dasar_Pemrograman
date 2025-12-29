def calculate_risk(data):
    """
    Menghitung skor risiko diabetes berdasarkan BMI,
    usia, riwayat keluarga, dan aktivitas fisik.
    """

    # BMI
    height_m = data["height"] / 100
    bmi = data["weight"] / (height_m ** 2)

    score = 0

    # Penilaian BMI
    if bmi < 18.5:
        score += 10
    elif bmi < 25:
        score += 20
    elif bmi < 30:
        score += 40
    else:
        score += 60

    # Usia
    if data["age"] > 45:
        score += 20
    elif data["age"] > 30:
        score += 10

    # Riwayat keluarga
    if data["family_history"] == "Ya":
        score += 15

    # Aktivitas fisik
    activity_score = {
        "Rendah": 20,
        "Sedang": 10,
        "Tinggi": 0
    }
    score += activity_score[data["activity_level"]]

    return min(score, 100)


def risk_category(score):
    if score < 30:
        return "Rendah"
    elif score < 60:
        return "Sedang"
    else:
        return "Tinggi"