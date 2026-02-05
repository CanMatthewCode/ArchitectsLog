from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

class AnalyticsChartDesigner(FigureCanvasQTAgg):
	"""Class to create Matplotlib charts for Analytics windows"""
	def __init__(self, parent=None) -> None:
		self.fig = Figure()
		super().__init__(self.fig)
		self.fig.patch.set_facecolor('#1E2E34')  # Figure background
		
		self.PHASE_NAMES_SHORT = [
			"Schem Design",
			"Design Dev.", 
			"Construct Doc.", 
			"Bid Negotiation", 
			"Construct Admin.",
			"Interior Design",
			"Add Service",
			"Business Dev.",
			"Administration"
			]
		self.PHASE_NAMES_LONG = [
			"Schematic Design", 
			"Design Development", 
			"Construction Documents", 
			"Bidding Negotiation", 
			"Construction Administration",
			"Interior Design",
			"Add Service",
			"Business Development",
			"Administration"
			]
		self.PHASE_COLORS = [
			'#ffffd9', 
			'#c7e9b4', 
			'#7fcdbb', 
			'#41b6c4', 
			'#3a9fc4', 
			'#2c7fb8', 
			'#2d5a8a', 
			'#aa99ff', 
			'#d47fff',
			]

	def bars_project_phase(self, data: list[tuple[int, int]]) -> None:
		"""Method for creating a bar chart for one project. data is list of tuples
		containing (phase_id, durations)"""
		self.ax = self.fig.add_subplot(111)
		self.ax.clear()
		self.ax.set_axisbelow(True)

		phase_ids = [row[0] for row in data]
		data_list = [row[1] for row in data]
		phase_name = [self.PHASE_NAMES_SHORT[phase_id - 1] for phase_id in phase_ids]
		colors = [self.PHASE_COLORS[phase_id - 1] for phase_id in phase_ids]

		x_positions = range(len(phase_ids))
		bars = self.ax.bar(x_positions, data_list, color=colors)

		self.ax.bar_label(bars, label_type='edge', 
			color = 'white', fontsize=8)
		self.ax.set_facecolor('#2A3F45')  # Plot area
		self.ax.spines['bottom'].set_color('#4A6F75')
		self.ax.spines['left'].set_color('#4A6F75')
		self.ax.spines['top'].set_visible(False)
		self.ax.spines['right'].set_visible(False)

		self.ax.tick_params(axis='x', rotation=15, labelsize=8, colors='#89D5D2')
		self.ax.tick_params(axis='y', labelsize=8, colors='#89D5D2')

		self.ax.set_xticks(x_positions)
		self.ax.set_xticklabels(phase_name, ha='right')

		#self.ax.set_title('Phase Hours Breakdown', color='#89D5D2', pad=20)
		self.fig.suptitle('Phase Hours Breakdown', color='#89D5D2', fontsize=12, y=0.97)
		self.ax.set_ylabel('Total Hours', color='#89D5D2')

		self.draw()

	def pie_project_phase(self, data: list[tuple[int, int]]) -> None:
		"""Method for creating a pie chart for one project. data is list of tuples
		containing (phase_id, durations)"""
		self.ax = self.fig.add_subplot(111)
		self.ax.clear()
		
		self.ax.set_position([0.4, 0.1, 0.5, 0.8])
		self.fig.suptitle('Phase Hours Breakdown', color='#89D5D2', fontsize=12, y=0.96)

		phase_ids = [row[0] for row in data]
		data_list = [row[1] for row in data]
		phase_name = [self.PHASE_NAMES_LONG[phase_id - 1] for phase_id in phase_ids]
		colors = [self.PHASE_COLORS[phase_id - 1] for phase_id in phase_ids]

		explode = [0.05 if v < 5 else 0 for v in data_list]

		wedges, texts, autotexts = self.ax.pie(
			data_list, 
			autopct="%1.1f%%", 
			colors=colors,
			explode=explode,
			startangle=90,
			counterclock=False,
			textprops=dict(color='black', fontsize=8, fontweight='bold'),
			pctdistance=0.8)

		legend = self.ax.legend(
			wedges, phase_name, 
			title="Phases", 
			loc="center left", 
			bbox_to_anchor=(1, 0, 0.5, 1),
			prop={'size': 10},
			facecolor='#A0E0DD',
			edgecolor='#1E2E34'
			)

		legend.get_title().set_fontsize(12)
		legend.get_title().set_weight('bold')

		self.fig.tight_layout()

		self.draw()
