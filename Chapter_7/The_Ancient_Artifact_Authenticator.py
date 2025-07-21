
class ArtifactAuthenticationError(Exception):
    """Custom exception for artifact authentication failures."""
    pass

def authenticate_relic(relic_name: str, purity_score: int, origin_sealed: bool):
    """
    Authenticates an ancient relic based on its properties.
    Raises specific errors if authentication fails.
    """
    print(f"\n--- Authenticating Relic: '{relic_name}' ---")
    if not isinstance(relic_name, str) or not relic_name:
        raise TypeError("Relic name must be a non-empty string.")
    if not isinstance(purity_score, int) or not (0 <= purity_score <= 100):
        raise ValueError("Purity score must be an integer between 0 and 100.")

    if purity_score < 70:
        raise ArtifactAuthenticationError(f"Relic '{relic_name}' has insufficient purity ({purity_score}%). Authentication failed!")
    if not origin_sealed:
        raise ArtifactAuthenticationError(f"Relic '{relic_name}' origin not sealed. Authentication failed!")

    print(f"  Relic '{relic_name}' (Purity: {purity_score}%, Origin Sealed: {origin_sealed}) is AUTHENTIC!")
    return True

# --- Testing the Authenticator ---
try:
    authenticate_relic("Amulet of Truth", 95, True) # Authentic
except (TypeError, ValueError, ArtifactAuthenticationError) as e:
    print(f"Authentication Failed: {e}")

try:
    authenticate_relic("Corrupted Blade", 65, True) # Low purity
except (TypeError, ValueError, ArtifactAuthenticationError) as e:
    print(f"Authentication Failed: {e}")

try:
    authenticate_relic("Unsealed Scroll", 80, False) # Origin not sealed
except (TypeError, ValueError, ArtifactAuthenticationError) as e:
    print(f"Authentication Failed: {e}")

try:
    authenticate_relic(123, 90, True) # Incorrect type for name
except (TypeError, ValueError, ArtifactAuthenticationError) as e:
    print(f"Authentication Failed: {e}")