from flask_smorest import Blueprint
from flask.views import MethodView
import random

blp = Blueprint(
    "Quote",
    "quote",
    url_prefix="/api",
    description="Endpoints for retrieving motivational quotes"
)

_QUOTES = [
    {"quote": "The only way to do great work is to love what you do.",
     "author": "Steve Jobs"},
    {"quote": "Believe you can and you're halfway there.",
     "author": "Theodore Roosevelt"},
    {"quote": "Success is not in what you have, but who you are.",
     "author": "Bo Bennett"},
    {"quote": "Keep your face always toward the sunshine—and shadows will fall behind you.",
     "author": "Walt Whitman"},
    {"quote": "Opportunities don't happen, you create them.",
     "author": "Chris Grosser"},
    {"quote": "It does not matter how slowly you go as long as you do not stop.",
     "author": "Confucius"},
    {"quote": "Everything you can imagine is real.",
     "author": "Pablo Picasso"},
    {"quote": "Make each day your masterpiece.",
     "author": "John Wooden"}
]


# PUBLIC_INTERFACE
@blp.route("/quote")
class QuoteResource(MethodView):
    """
    Get a random motivational quote.
    ---
    get:
        summary: Get a random motivational quote
        description: Returns a random motivational quote with its author
        responses:
            200:
                description: A JSON object with a quote and its author
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                quote:
                                    type: string
                                    description: The motivational quote
                                author:
                                    type: string
                                    description: The author of the quote
                            required:
                                - quote
                                - author
    """
    def get(self):
        """Return a random motivational quote and its author."""
        quote = random.choice(_QUOTES)
        return quote, 200
