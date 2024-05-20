from typing import List

from service.models import SongCategory


def decode_preferences(preference_decimal: int) -> List[str]:
    """
    Decodes a decimal representation of user preferences into a list of category names.

    This function takes a decimal number where each bit represents a specific category
    and converts it back to a list of category names using bitwise operations.

    Args:
        preference_decimal (int): The decimal representation of the user's preferences.

    Returns:
        List[str]: A list of category names that correspond to the set bits in the input decimal number.

    Example:
        >>> decode_preference(5)
        ['ELECTRONIC', 'HIPHOP']

    Explanation:
        If the input `preference_decimal` is 5, its binary representation is `101`.
        This means that the user has selected the categories corresponding to the 1st and 3rd bits:
        - ELECTRONIC (bit 1)
        - HIPHOP (bit 3)
    """
    return [
        category.name
        for category in SongCategory
        if preference_decimal & (1 << category.value)
    ]


def encode_preferences(user_preferences: List[SongCategory]) -> int:
    """
    Encodes a list of user preferences into a single integer using bitwise operations.

    This function takes a list of `SongCategory` enums representing the user's preferences and
    converts it into a single integer where each bit represents a specific category.

    Args:
        user_preferences (List[SongCategory]): A list of `SongCategory` enums representing the user's preferences.

    Returns:
        int: The decimal representation of the user's preferences, where each bit set to 1 indicates a selected category.

    Example:
        >>> encode_preference([SongCategory.ELECTRONIC, SongCategory.HIPHOP])
        5

    Explanation:
        If the input `user_preferences` contains `ELECTRONIC` and `HIPHOP`, their corresponding values are 1 and 3.
        The binary representation will be `101` (1 << 0 for ELECTRONIC and 1 << 2 for HIPHOP).
        The resulting decimal value is 5.
    """
    return sum((1 << SongCategory[category].value) for category in user_preferences)
