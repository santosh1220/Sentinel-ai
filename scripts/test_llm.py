from app.llm.client import LLMClient


def main() -> None:
    llm = LLMClient()

    question = "What should I do if I receive a phishing email?"

    context = """
    [Source 1: security_policy.pdf, page 1]
    Employees must report phishing emails to the security team immediately.

    [Source 2: security_policy.pdf, page 2]
    Security incidents must be reported to the SOC within 30 minutes.
    """

    answer = llm.generate_answer(
        question=question,
        context=context,
    )

    print(f"\nQuestion: {question}")
    print(f"\nSentinelAI Answer:\n{answer}")


if __name__ == "__main__":
    main()