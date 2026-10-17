from config import TORUN_CENTER


def infer_location(text: str) -> tuple[float, float]:
    value = text.lower()

    if "most" in value or "piłsud" in value or "rapack" in value:
        return 53.0055, 18.6003

    if "chełm" in value or "bema" in value:
        return 53.0195, 18.5985

    if "bydgos" in value or "gagarin" in value or "umk" in value:
        return 53.0152, 18.5815

    if "lubic" in value or "skarp" in value:
        return 53.0205, 18.654

    return TORUN_CENTER["lat"], TORUN_CENTER["lng"]
