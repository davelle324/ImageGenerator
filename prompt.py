import openai
import click

openai.api_key = "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"

def generate_response(prompt):
    """ Generate an AI response
        PROMPT is the prompt to give the AI
    """
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,
        temperature=0.6,
        n = 1,
        stop=None,
    )
    return response.choices[0].text.strip()

@click.command()
@click.option('--prompt', default="Say hello and ask what user would like", help="Input prompt to AI")
def cli(prompt):
    response = generate_response(prompt)
    print(response)
    
if __name__ == "__main__":
    cli()
