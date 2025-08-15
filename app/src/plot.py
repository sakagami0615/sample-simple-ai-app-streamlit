import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from src.model import Result


WEDGEPROPS = {"width": 0.3, "edgecolor": "white"}
TEXTPROPS = {"fontsize": 6}
AUTOPCT = "%.2f"


def draw_result_pie_diagram(results: list[Result], n_top: int=3) -> Figure:
    """円グラフの描画"""
    pie_labels = [result.classes_en for result in results[:n_top]]
    pie_labels.append("others")

    pie_probs = [result.prob for result in results[:n_top]]
    pie_probs.append(sum([result.prob for result in results[n_top:]]))      # TOP以外のprobの合計値を追加

    fig, ax = plt.subplots()

    ax.pie(
        pie_probs,
        labels=pie_labels,
        counterclock=False,
        startangle=90,
        textprops=TEXTPROPS,
        autopct=AUTOPCT,
        wedgeprops=WEDGEPROPS)

    return fig