import numpy as np

def final_disk_speed(height: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    """
    With the assumptions that the disk is in a system on earth (gravity is 9.81) 
    and that there is no kinetic friction when the disk is rolling without slipping,
    we can find the equation for the final velocity of the disk through the conservation of energy equations: 
        mgh = 1/2mv^2 + 1/2Iw^2
    Since the rolling object is a disk, the moment of inertia around it's center is 1/2mr^2, and the angular velocity w = v/r
        mgh = 1/2mv^2 + 1/2[1/2mr^2 ][v/r]^2
    This equation can be further simplified: 
        mgh = 1/2 mv^2 + 1/4mv^2
    Solving for v: 
        v = sqrt(4/3gh)

    Since this equation is only dependent on one variable, I went ahead and removed the rest of the parameters from the function. 
    """
    GRAVITY = 9.81

    if height < 0: 
        raise ValueError("Height cannot be negative")
    
    return np.sqrt((4.0/3.0) * GRAVITY * height)
