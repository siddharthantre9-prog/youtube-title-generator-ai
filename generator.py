import random

templates = [
    "Top 10 {car_type} in India {year} | Best {feature}",
    "{car_model} Review: Shocking Truth You Must Know!",
    "Best {car_type} Under {budget} | Don’t Buy Before Watching"
]

data = {
    "car_type": "SUV",
    "year": "2026",
    "feature": "Mileage",
    "car_model": "Hyundai Creta",
    "budget": "10 Lakh"
}

template = random.choice(templates)
title = template.format(**data)

print("Generated Title:")
print(title)
