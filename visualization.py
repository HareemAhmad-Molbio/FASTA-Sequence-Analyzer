import matplotlib.pyplot as plt
from pathlib import Path

FRAME_COLORS = {
    1: "#4CAF50",
    2: "#FF9800",
    3: "#2196F3",
}

LONGEST_COLOR = "#D32F2F"

def draw_title(ax):
    """Draw the figure title."""

    ax.set_title(
        "Open Reading Frame (ORF) Map",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )


def draw_genome_axis(ax, sequence_length):
    """Draw the genome coordinate axis."""

    ax.set_xlim(0, sequence_length)

    ax.set_xlabel(
        "Genome Position (bp)",
        fontsize=12,
    )

    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.3,
    )

def draw_gene(ax, start, length, y, color):
    """Draw one ORF as an arrow."""

    ax.arrow(
        start,
        y,
        length,
        0,
        width=0.08,
        head_width=0.22,
        head_length=max(length * 0.05, 50),
        length_includes_head=True,
        color=color,
    )


def draw_legend(ax):

    from matplotlib.patches import Patch

    legend = [

        Patch(
            color=FRAME_COLORS[1],
            label="Frame +1",
        ),

        Patch(
            color=FRAME_COLORS[2],
            label="Frame +2",
        ),

        Patch(
            color=FRAME_COLORS[3],
            label="Frame +3",
        ),

        Patch(
            color=LONGEST_COLOR,
            label="Longest ORF",
        ),
    ]

    ax.legend(
        handles=legend,
        loc="upper right",
    )    


def plot_nucleotide_counts(counts, output_file):
    """
    Generate a publication-quality bar chart of nucleotide composition.
    """

    bases = ["A", "T", "G", "C"]
    values = [counts.get(base, 0) for base in bases]

    plt.figure(figsize=(8, 5))

    colors = [
        "#4CAF50",   # A
        "#F44336",   # T
        "#FF9800",   # G
        "#2196F3",   # C   
    ]

    bars = plt.bar(
        bases,
        values,
        color=colors,
        edgecolor="black",
        linewidth=1,
    )

    plt.title(
        "DNA Nucleotide Composition",
        fontsize=16,
        fontweight="bold",
    )

    plt.xlabel("Nucleotide", fontsize=12)

    plt.ylabel("Count", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    # Add values above each bar
    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,}",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.tight_layout()

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

def plot_gc_content(positions, gc_values, output_file):
    """
    Plot sliding-window GC content across the sequence.
    """

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        positions,
        gc_values,
        linewidth=2,
        color="#2E7D32",
    )

    ax.fill_between(
        positions,
        gc_values,
        alpha=0.25,
        color="#66BB6A",
    )

    ax.set_title(
        "Sliding Window GC Content",
        fontsize=18,
        fontweight="bold",
    )

    ax.set_xlabel(
        "Genome Position (bp)",
        fontsize=12,
    )

    ax.set_ylabel(
        "GC Content (%)",
        fontsize=12,
    )

    ax.set_ylim(0, 100)

    ax.grid(
        linestyle="--",
        alpha=0.3,
    )

    plt.tight_layout()

    output_path = Path(output_file)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    plt.savefig(
        output_path.with_suffix(".svg"),
        bbox_inches="tight",
    )

    plt.close()

def plot_orf_overview(orfs_by_frame, sequence_length, output_file):
    """
    Generate a publication-style ORF map.
    """

    fig, ax = plt.subplots(figsize=(14, 5))

    draw_title(ax)

    draw_genome_axis(ax, sequence_length)

    longest = get_longest_orf(orfs_by_frame)

    FRAME_Y = {
        "Frame +1": 3,
        "Frame +2": 2,
        "Frame +3": 1,
    }

    FRAME_NUMBER = {
        "Frame +1": 1,
        "Frame +2": 2,
        "Frame +3": 3,
    }

    for frame_name, orfs in orfs_by_frame.items():

        y = FRAME_Y[frame_name]

        frame_number = FRAME_NUMBER[frame_name]

        for orf in orfs:

            if orf is longest:
                color = LONGEST_COLOR
            else:
                color = FRAME_COLORS[frame_number]

            draw_gene(
                ax,
                orf["start"],
                orf["length"],
                y,
                color,
            )

    ax.set_ylim(0.5, 3.5)

    ax.set_yticks([1, 2, 3])

    ax.set_yticklabels([
        "Frame +3",
        "Frame +2",
        "Frame +1",
    ])

    draw_legend(ax)

    plt.tight_layout()

    output_path = Path(output_file)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    svg_path = output_path.with_suffix(".svg")

    plt.savefig(
        svg_path,
        bbox_inches="tight",
    )

    plt.close()

def plot_orf_comparison(orfs_by_frame, output_file):
    """
    Compare the longest ORF from each reading frame.
    """

    fig, ax = plt.subplots(figsize=(12, 6))

    y_positions = {
        "Frame +1": 3,
        "Frame +2": 2,
        "Frame +3": 1,
    }

    max_length = 0

    longest_orfs = []

    for frame_name, orfs in orfs_by_frame.items():

        if not orfs:
            continue

        longest = max(orfs, key=lambda x: x["length"])

        longest_orfs.append((frame_name, longest))

        if longest["length"] > max_length:
            max_length = longest["length"]

    for frame_name, orf in longest_orfs:

        y = y_positions[frame_name]

        frame_number = int(frame_name[-1])

        draw_gene(
            ax,
            0,
            orf["length"],
            y,
            FRAME_COLORS[frame_number],
        )

        ax.text(
            orf["length"] + max_length * 0.03,
            y,
            f'{orf["length"]} bp',
            va="center",
            fontsize=11,
            fontweight="bold",
        )

        ax.text(
            0,
            y - 0.28,
            f'{orf["start"]} → {orf["end"]}',
            fontsize=9,
        )

    ax.set_xlim(0, max_length * 1.25)

    ax.set_ylim(0.5, 3.5)

    ax.set_yticks([1, 2, 3])

    ax.set_yticklabels([
        "Frame +3",
        "Frame +2",
        "Frame +1",
    ])

    ax.set_xlabel("ORF Length (bp)")

    ax.set_title(
        "Longest ORFs by Reading Frame",
        fontsize=18,
        fontweight="bold",
    )

    ax.grid(axis="x", linestyle="--", alpha=0.3)

    draw_legend(ax)

    plt.tight_layout()

    output_path = Path(output_file)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    plt.savefig(
        output_path.with_suffix(".svg"),
        bbox_inches="tight",
    )

    plt.close()

def get_longest_orf(orfs_by_frame):
    """
    Return the longest ORF across all frames.
    """

    longest = None

    for frame_orfs in orfs_by_frame.values():

        for orf in frame_orfs:

            if longest is None:
                longest = orf

            elif orf["length"] > longest["length"]:
                longest = orf

    return longest