# Gravitational constant
G = 6.674 * 10**-11  # Nm^2/kg^2

def gravitational_force(m1, m2, r):
    """
    Calculate the gravitational force between two objects.
    
    Parameters:
    m1 : float : Mass of the first object in kilograms.
    m2 : float : Mass of the second object in kilograms.
    r  : float : Distance between the centers of the two masses in meters.
    
    Returns:
    float : Gravitational force in Newtons (N).
    """
    # Calculate the force
    force = G
   