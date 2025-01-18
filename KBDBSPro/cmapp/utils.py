from .models import currencystate


def get_currency_state():   
    # Retrieve the first record from the CurrencyState model
    currency_state_obj = currencystate.objects.first()

    if not currency_state_obj:
        return {}  # Return an empty dictionary if no record exists

    # Mapping fields from the model to a dictionary
    currency_state = {
        'fivehundred': currency_state_obj.fivehundred,
        'twohundred': currency_state_obj.twohundred,
        'onehundred': currency_state_obj.onehundred,
        'fifty': currency_state_obj.fifty,
        'twenty': currency_state_obj.twenty,
        'ten': currency_state_obj.ten,
        'five': currency_state_obj.five,
        'two': currency_state_obj.two,
        'one': currency_state_obj.one,
    }
    return currency_state  # Return the dictionary, not the model class


def display_bal():
    # Retrieve the currency state using the get_currency_state function
    currency_state = get_currency_state()

    if not currency_state:
        return {"message": "No currency state available.", "total": 0}

    # Mapping from string denominations to numeric values
    denomination_mapping = {
        'fivehundred': 500,
        'twohundred': 200,
        'onehundred': 100,
        'fifty': 50,
        'twenty': 20,
        'ten': 10,
        'five': 5,
        'two': 2,
        'one': 1
    }

    # Initialize results
    denomination_details = {}
    total_balance = 0
    total_notes = 0

    # Calculate the total balance, breakdown, and total notes
    for denomination, count in currency_state.items():
        # Ensure the count is an integer, defaulting to 0 if it's None
        count = count or 0

        # Convert denomination to numeric value using the mapping
        numeric_denomination = denomination_mapping.get(denomination)
        if numeric_denomination:
            # Calculate the total for each denomination
            total_for_denomination = numeric_denomination * count
            denomination_details[numeric_denomination] = {
                "count": count,
                "total": total_for_denomination
            }

            # Add to the overall totals
            total_balance += total_for_denomination
            total_notes += count

    # Prepare the result
    bal_result = {
        "denomination_details": denomination_details,
        "total_balance": total_balance,
        "total_notes": total_notes
    }
    return bal_result
