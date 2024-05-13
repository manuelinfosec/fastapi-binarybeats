# BinaryBeats

BinaryBeats is a project designed to optimize the storage and retrieval of user song preferences using advanced binary encoding techniques. This project uses FastAPI for its simplicity in building the API.

## Approach

### Encoding User's Song Preferences into Binary

1. **Genre Representation**:
   - Each song is associated with one or more genres, such as electronic, jazz, hip-hop, etc.
   - We represent each genre using a binary digit, where 1 indicates the presence of the genre and 0 indicates the absence.

2. **Binary Representation**:
   - We encode the user's song preferences into a compact binary representation.
   - Each binary digit corresponds to a specific genre, with 1 representing the user's preference for that genre and 0 indicating no preference.
   - For example, if a user prefers electronic and hip-hop but not jazz, the binary representation would be something like `101`.

### Conversion to Decimal and Storage

1. **Decimal Representation**:
   - To efficiently store the binary representation in the database, it's converted to its decimal-equivalent.
   - The decimal value represents the combined preferences of the user for all genres.

2. **Storage**:
   - We store the decimal representation of the user's preferences in the database for easy retrieval and manipulation.

### Bitwise Operation for Filtering Matching Songs

1. **Matching Songs**:
   - When a user requests song recommendations, we perform bitwise operations between the stored decimal representation of their preferences and the binary representation of each song's genres.
   - If the result of the bitwise AND operation is non-zero, it indicates a match between the user's preferences and the song's genres.

2. **Efficiency**:
   - By using bitwise operations, we efficiently filter out songs that do not match the user's preferences, reducing the computational overhead and improving performance. Bitwise operations are highly efficient, typically taking only one CPU cycle to complete.

## Technical Theory

- **Binary Representation**: Binary encoding allows us to represent complex data using a sequence of binary digits, enabling efficient storage and manipulation.
- **Decimal Conversion**: Converting the binary representation to decimal simplifies storage and retrieval, as most databases support efficient storage and querying of decimal values.
- **Bitwise Operations**: Bitwise AND operation allows us to compare individual bits of two binary numbers, enabling us to identify matching genres between the user's preferences and song categories.

## Credits 
Inspired by the video from [TheWisePup](https://vm.tiktok.com/ZMM7SsDUv/).
