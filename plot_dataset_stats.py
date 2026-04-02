"""
Dataset statistics plots for the bachelor thesis.
Run this script to regenerate all figures in images/.

To update values: edit DATASETS below.
To add a dataset: add a new entry to DATASETS and COLORS.
"""

import plotly.graph_objects as go

# ── Data ──────────────────────────────────────────────────────────────────────
# Annotation instance counts per unified class.
# Use 0 for classes absent in a dataset.
# Order must match CLASSES.

CLASSES = ["Car", "Bus", "Truck", "Motorcycle", "Person"]

DATASETS = {
    "DroneVehicle": [440_163,  16_535, 43119,     0,     0],  # car includes van; truck includes freight car
    "RTDOD":        [78_063,  2_336,  7_580,  26_378, 57_515],
    "M3FD":         [18_296,  700,  1_008,  521,  11_477],
    "Ours":         [  450,   120,   230,     0,     0],  # placeholder — update when collection is complete
}

COLORS = {
    "DroneVehicle": "#1D4ED8",  # blue-700
    "RTDOD":        "#C2410C",  # orange-700
    "M3FD":         "#047857",  # emerald-700
    "Ours":         "#6D28D9",  # violet-700
}

FONT    = "Helvetica Neue, Arial, sans-serif"
GRAY_HI = "#111827"
GRAY_LO = "#6B7280"

# Approximate inner plot height in pixels — used to decide which labels fit inside a segment.
# Adjust if the figure height changes significantly.
PLOT_H_PX    = 400
MIN_LABEL_PX = 14  # min segment height in px to show a label inside


# ── Plot: class distribution ───────────────────────────────────────────────────
def plot_class_distribution():
    totals = [
        sum(DATASETS[ds][i] for ds in DATASETS)
        for i in range(len(CLASSES))
    ]
    y_max = max(totals) * 1.14
    px_per_unit = PLOT_H_PX / y_max

    fig = go.Figure()

    for ds_name, counts in DATASETS.items():
        text = [
            f"{c:,}" if c > 0 and c * px_per_unit >= MIN_LABEL_PX else ""
            for c in counts
        ]
        fig.add_trace(go.Bar(
            name=ds_name,
            x=CLASSES,
            y=counts,
            text=text,
            textposition="inside",
            insidetextanchor="middle",
            marker_color=COLORS[ds_name],
            marker_line_color="rgba(255,255,255,0.6)",
            marker_line_width=0.5,
            marker_cornerradius=4,
            textfont=dict(color="white", size=10, family=FONT),
        ))

    # Build annotations: total above every bar, plus a color-coded breakdown
    # of any segments too small to label inside.
    annotations = []
    for i, cls in enumerate(CLASSES):
        total = totals[i]

        # Collect hidden labels, top segment first (reversed dataset order).
        hidden = []
        for ds_name, counts in reversed(list(DATASETS.items())):
            count = counts[i]
            if count > 0 and count * px_per_unit < MIN_LABEL_PX:
                c = COLORS[ds_name]
                hidden.append(f"<span style='color:{c}'>{count:,}</span>")

        if hidden:
            text = f"<b>{total:,}</b><br>" + "<br>".join(hidden)
            font_size = 9.5
        else:
            text = f"<b>{total:,}</b>"
            font_size = 11

        annotations.append(dict(
            x=cls, y=total,
            text=text,
            showarrow=False,
            yanchor="bottom",
            yshift=6,
            font=dict(size=font_size, color=GRAY_HI, family=FONT),
            align="center",
        ))

    fig.update_layout(
        barmode="stack",
        bargap=0.25,
        template="simple_white",
        font=dict(family=FONT, size=12, color=GRAY_HI),
        plot_bgcolor="white",
        paper_bgcolor="white",
        yaxis=dict(
            title=dict(
                text="Number of Instances",
                font=dict(size=12, color=GRAY_LO),
                standoff=12,
            ),
            tickformat=",",
            tickfont=dict(size=11, color=GRAY_LO),
            showgrid=True,
            gridcolor="#e0e0e0",
            gridwidth=1,
            zeroline=False,
            showline=True,
            linecolor="#d0d0d0",
            linewidth=1,
            range=[0, y_max],
        ),
        xaxis=dict(
            title=None,
            tickfont=dict(size=13, color=GRAY_HI),
            showline=True,
            linecolor="#d0d0d0",
            linewidth=1,
            ticklen=0,
        ),
        legend=dict(
            title=dict(text="Dataset", font=dict(size=12, color=GRAY_HI)),
            bgcolor="rgba(255,255,255,0.92)",
            bordercolor="#e0e0e0",
            borderwidth=1,
            font=dict(size=12),
            x=0.99, xanchor="right",
            y=0.99, yanchor="top",
            traceorder="normal",
        ),
        uniformtext=dict(mode="hide", minsize=9),
        annotations=annotations,
        width=780,
        height=500,
        margin=dict(l=70, r=30, t=40, b=55),
    )

    fig.write_image("images/dataset_class_distribution.pdf")
    fig.write_image("images/dataset_class_distribution.png", scale=2)
    print("Saved: images/dataset_class_distribution.{pdf,png}")


if __name__ == "__main__":
    plot_class_distribution()
