"""  MA4_1.1

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Joacim Stenlund
Date reviewed: 16/05
"""

import matplotlib.pyplot as plt
import random
import math


def multi_plot():
    """runs all tests a once and plots in same figure"""

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)

    subplot = {ax1: 1000, ax2: 10000, ax3: 100000}

    for ax in subplot:
        N = subplot[ax]
        ax.set_aspect("equal", adjustable="box")
        ax.set_title(f"No. dots: {N}")
        Nc = 0

        for _ in range(N):
            x, y = random.uniform(-1, 1), random.uniform(-1, 1)

            if x**2 + y**2 <= 1:
                Nc += 1
                ax.plot(
                    x,
                    y,
                    marker="o",
                    markersize=1,
                    markeredgecolor="#FF0000",
                    markerfacecolor="#FF0000",
                )
            else:
                ax.plot(
                    x,
                    y,
                    marker="o",
                    markersize=1,
                    markeredgecolor="#0000FF",
                    markerfacecolor="#0000FF",
                )

        print("\n-----------------------------------------------------\n")
        print(
            f"""Number of dots in circle: {Nc}
Estimated value of pi: {4*(Nc/N)}
Theoretical value: {math.pi}
        """
        )
        print("\n-----------------------------------------------------\n")

    plt.show()


def input_plot():
    """runs all test from input and plots results"""
    print("\n-----------------------------------------------------\n")
    N = int(input(f"How many dots?: "))
    print("\n\n")

    Nc = 0

    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(f"No. dots: {N}")

    # skapa listor och klra scatterplot, 2ggr

    for _ in range(N):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            Nc += 1
            ax.plot(
                x,
                y,
                marker="o",
                markersize=1,
                markeredgecolor="#FF0000",
                markerfacecolor="#FF0000",
            )
        else:
            ax.plot(
                x,
                y,
                marker="o",
                markersize=1,
                markeredgecolor="#0000FF",
                markerfacecolor="#0000FF",
            )

    plt.show()

    print(
        f"""Number of dots in circle: {Nc}
Estimated value of pi: {4*(Nc/N)}
Theoretical value: {math.pi}
"""
    )
    print("\n-----------------------------------------------------\n")


def main():
    multi_plot()
    # input_plot()


if __name__ == "__main__":
    main()

# Results of executing multi_plot()
"""
-----------------------------------------------------

Number of dots in circle: 770
Estimated value of pi: 3.08
Theoretical value: 3.141592653589793
        

-----------------------------------------------------


-----------------------------------------------------

Number of dots in circle: 7908
Estimated value of pi: 3.1632
Theoretical value: 3.141592653589793
        

-----------------------------------------------------


-----------------------------------------------------

Number of dots in circle: 78587
Estimated value of pi: 3.14348
Theoretical value: 3.141592653589793
        

-----------------------------------------------------
"""
