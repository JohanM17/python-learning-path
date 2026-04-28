nota: int = 85

if nota >= 90:
    print("Excelente, eres un buen estudiante")
elif nota >= 70:       # Ya sabemos que es < 90 porque el if anterior falló
    print("Muy bien, aprobó")
elif nota >= 50:       # Ya sabemos que es < 70
    print("Raspando.")
else:
    print("Reprobó, debe recuperar")
