"""Planning calculator. USD prices checked 2026-09-24; FX is an assumption."""
import argparse

RATES = {"gpt-4o": (2.5, 10.0), "gpt-4.1-mini": (0.4, 1.6)}


def estimate(model, questions, calls, input_tokens, output_tokens):
    incoming, outgoing = RATES[model]
    return questions * calls * (input_tokens * incoming + output_tokens * outgoing) / 1_000_000


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--model", choices=RATES, default="gpt-4.1-mini")
    p.add_argument("--questions", type=int, default=300)
    p.add_argument("--calls", type=int, default=3)
    p.add_argument("--input-tokens", type=int, default=2500)
    p.add_argument("--output-tokens", type=int, default=500)
    p.add_argument("--aud-per-usd", type=float, default=1.55)
    p.add_argument("--vm-hours", type=float, default=0)
    p.add_argument("--vm-usd-per-hour", type=float, default=0)
    p.add_argument("--storage-usd", type=float, default=0)
    p.add_argument("--vector-usd", type=float, default=0)
    args = p.parse_args()
    if any(v < 0 for k, v in vars(args).items() if isinstance(v, (int, float))):
        p.error("Costs and usage cannot be negative.")
    api = estimate(args.model, args.questions, args.calls, args.input_tokens, args.output_tokens)
    total = api + args.vm_hours * args.vm_usd_per_hour + args.storage_usd + args.vector_usd
    print(f"Model: {args.model}; API estimate: US${api:.2f}")
    print(f"Total supplied costs: US${total:.2f} / AU${total * args.aud_per_usd:.2f}")
    print("Planning estimate, not a quote. FX is user-supplied/assumed; tax, embeddings and unspecified services excluded.")
