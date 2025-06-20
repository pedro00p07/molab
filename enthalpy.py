def verificar_entalpia(entalpia_valor: float) -> str:
    if entalpia_valor < 0:
        return (
            "🔵 Reação exotérmica (ΔH < 0).\n"
            "⚠ Tome as medidas de EPI necessárias.\n"
            "💡 Controle bem a temperatura do ambiente da reação.\n"
            "📘 Calcule estequiometricamente e avalie a variação de entalpia.\n"
            "✅ Verifique se há alternativas mais seguras para a reação."
        )
    elif entalpia_valor > 0:
        return (
            "🔴 Reação endotérmica (ΔH > 0).\n"
            "⚠ Tome as medidas de EPI necessárias.\n"
            "💡 Controle a temperatura e fornecimento de calor adequados.\n"
            "📘 Calcule estequiometricamente e avalie a viabilidade energética.\n"
            "✅ Avalie se há métodos mais eficientes para obter o mesmo produto."
        )
    else:
        return "ℹ Entalpia nula ou não determinada."
