from transformers import pipeline

PREDEFINED_ANSWERS = {
    "игрушки 3 месяца": "Для ребёнка в 3 месяца подойдут мягкие погремушки, развивающие коврики, мобили на кроватку, игрушки с разными текстурами и звуками.",
    "питание 6 месяцев": "В 6 месяцев можно вводить прикорм: овощные пюре, каши без глютена, постепенно фрукты.",
    "сон 1 год": "В этом возрасте ребёнку нужно около 11–12 часов ночного сна и 1–2 дневных сна по 1–2 часа.",
    "температура у ребенка": "Если у ребёнка температура выше 38°C и он вялый — обратись к педиатру. Следи за состоянием, давай воду.",
    "как приучить к горшку": "Не торопитесь. Начинайте, когда ребёнок показывает интерес. Делайте процесс игровым и хвалите за успехи.",
}


print("🔁 Загружаю AI модель...")
generator = pipeline("text-generation", model="ai-forever/rugpt3small_based_on_gpt2")

def generate_answer(question):
    question_lower = question.lower()
    for keyword, predefined in PREDEFINED_ANSWERS.items():
        if all(word in question_lower for word in keyword.split()):
            return predefined


    prompt = f"Ты — заботливый помощник родителям. Отвечай чётко и по делу. Вопрос: {question} Ответ:"
    result = generator(
        prompt,
        max_length=60,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8,
        repetition_penalty=1.2,
    )[0]['generated_text']
    return result.split("Ответ:")[-1].strip()