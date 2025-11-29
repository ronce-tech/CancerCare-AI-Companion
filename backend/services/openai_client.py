import asyncio

# Temporary fake AI implementation (real OpenAI comes later)

CANCERCARE_PERSONA = """
You are CancerCare AI, an educational and emotional support companion.
You DO NOT diagnose, interpret medical exams, or give medical decisions.
You explain calmly, clearly, and always advise seeing a doctor.
"""

async def get_cancercare_reply(user_message: str, locale: str, role: str) -> str:
    """Stub AI response"""
    await asyncio.sleep(0.1)

    if locale == "fr":
        return "Je suis CancerCare AI. Je peux expliquer des termes médicaux et t’aider à préparer des questions — mais je ne pose aucun diagnostic. (mode démo)"
    if locale == "es":
        return "Soy CancerCare AI. Puedo ayudar a entender términos médicos — pero no doy diagnósticos. (modo demo)"

    return "I am CancerCare AI. I can explain medical terms and help you prepare questions — but I do not diagnose anything. (demo mode)"
