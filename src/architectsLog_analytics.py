from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Patch
import matplotlib.dates as mdates

from datetime import datetime
from typing import Optional

from architectsLog_constants import BUSDEV

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
		self.PHASE_NAMES = [
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

	def bars_by_phase(self, data: list[tuple[int, int]],
		title: str = 'Phase Hours Breakdown') -> None:
		"""Method for creating a bar chart based on phases; data is list of tuples
		containing (phase_id, duration)"""
		self.ax = self.fig.add_subplot(111)
		self.ax.clear()

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

		self.fig.suptitle(title, color='#89D5D2', fontsize=12, y=0.97)
		self.ax.set_ylabel('Total Hours', color='#89D5D2')

		self.draw()

	def pie_by_phase(self, data: list[tuple[int, int]], 
		title: str = "Phase Hours Breakdown", show_admin: bool = True) -> None:
		"""Method for creating a pie chart based on phases; data is list of tuples
		containing (phase_id, duration). Pass in False to hide Business Dev/ Admin"""
		self.ax = self.fig.add_subplot(111)
		self.ax.clear()
		
		self.ax.set_position([0.4, 0.1, 0.5, 0.8])
		self.fig.suptitle(title, color='#89D5D2', fontsize=12, y=0.96)

		if show_admin:
			phase_ids = [row[0] for row in data]
			data_list = [row[1] for row in data]
		else:
			phase_ids = [row[0] for row in data if row[0] < BUSDEV]
			data_list = [row[1] for row in data if row[0] < BUSDEV]
		phase_name = [self.PHASE_NAMES[phase_id - 1] for phase_id in phase_ids]
		colors = [self.PHASE_COLORS[phase_id - 1] for phase_id in phase_ids]

		total_time = sum(data_list)
		explode = [0.03 if v/total_time < .04 else 0 for v in data_list]

		wedges, texts, autotexts = self.ax.pie(
			data_list, 
			autopct="%1.1f%%", 
			colors=colors,
			explode=explode,
			startangle=180,
			counterclock=False,
			textprops=dict(color='black', fontsize=8, fontweight='bold'),
			pctdistance=0.8)

		legend = self.ax.legend(
			wedges, phase_name, 
			title='Phases', 
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

	def stem_plot_phase(self, data: list[tuple[int, int, int]]) -> None:
		"""Method for creating a stem plot of time_entry duration_minutes
		plotted against time and color coded by phase_id"""
		self.ax = self.fig.add_subplot(111)
		self.ax.clear()
		self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
		self.ax.set_position([0.1, 0.1, 0.65, 0.8])

		phase_ids = [row[0] for row in data]
		duration_list = [row[1]/60 for row in data]
		start_times = [row[2] for row in data]
		dates = [datetime.fromtimestamp(time) for time in start_times]
		colors = [self.PHASE_COLORS[phase_id - 1] for phase_id in phase_ids]

		for date, duration, color in zip(dates, duration_list, colors):
			self.ax.stem([date], [duration], linefmt=color, markerfmt='.', basefmt=' ')

		self.ax.set_facecolor('#2A3F45')  # Plot area
		self.ax.spines['bottom'].set_color('#4A6F75')
		self.ax.spines['left'].set_color('#4A6F75')
		self.ax.spines['top'].set_visible(False)
		self.ax.spines['right'].set_visible(False)

		self.ax.tick_params(axis='x', rotation=15, labelsize=8, colors='#89D5D2')
		self.ax.tick_params(axis='y', labelsize=8, colors='#89D5D2')
		
		self.fig.suptitle('Phase Hours Over Time', color='#89D5D2',
			fontsize=12, x=.44, y=0.97)
		self.ax.set_ylabel('Hours', color='#89D5D2')

		unique_phases = sorted(set(phase_ids))
		legend_elements = [Patch(facecolor=self.PHASE_COLORS[pid-1], 
			label=self.PHASE_NAMES[pid-1]) 
 			for pid in unique_phases]
		legend = self.ax.legend(
			handles=legend_elements, 
			title="Phases", 
			loc="center left", 
			bbox_to_anchor=(1, 0, 0.5, 1),
			prop={'size': 9},
			facecolor='#A0E0DD',
			edgecolor='#1E2E34')
		legend.get_title().set_fontsize(11)
		legend.get_title().set_weight('bold')

		self.draw()

	def step_plot_phase(self, data: list[tuple[int, int, int]]) -> None:
		"""Method to create a step plot of time_entry duration minutes
		plotted against time and color code by phase_id"""
		self.ax = self.fig.add_subplot(111)
		self.ax.clear()
		self.ax.set_axisbelow(True)
		self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
		self.ax.set_position([0.1, 0.1, 0.65, 0.8])

		current_phase = data[0][0]
		temp_dates = [datetime.fromtimestamp(data[0][2])]
		temp_cumulative_time = [0]
		cumulative_time = 0
		phase_ids = []
		for item in data:
			if current_phase != item[0]:
				temp_date = temp_dates[-1]
				temp_time = temp_cumulative_time[-1]
				self.ax.step(temp_dates, temp_cumulative_time, 
					self.PHASE_COLORS[current_phase-1])
				current_phase = item[0]
				temp_dates.clear()
				temp_cumulative_time.clear()
				temp_dates.append(temp_date)
				temp_cumulative_time.append(temp_time)
			cumulative_time += item[1]/60
			x = datetime.fromtimestamp(item[2])
			self.ax.vlines(x, 0, cumulative_time, color=self.PHASE_COLORS[item[0]-1],
				linewidth=.9, alpha=.6)
			temp_cumulative_time.append(cumulative_time)
			temp_dates.append(datetime.fromtimestamp(item[2]))
			phase_ids.append(item[0])
		self.ax.step(temp_dates, temp_cumulative_time,
			self.PHASE_COLORS[current_phase-1])

		self.ax.set_facecolor('#2A3F45')  # Plot area
		self.ax.spines['bottom'].set_color('#4A6F75')
		self.ax.spines['left'].set_color('#4A6F75')
		self.ax.spines['top'].set_visible(False)
		self.ax.spines['right'].set_visible(False)
		self.ax.grid(color='#3A5F65', alpha=0.3, axis='x')
		self.ax.tick_params(axis='x', rotation=15, labelsize=8, colors='#89D5D2')
		self.ax.tick_params(axis='y', labelsize=8, colors='#89D5D2')
		
		self.fig.suptitle('Cumulative Hours Over Time', color='#89D5D2', 
			fontsize=12, x=.44, y=.97)
		self.ax.set_ylabel('Total Hours', color='#89D5D2')

		unique_phases = sorted(set(phase_ids))
		legend_elements = [Patch(facecolor=self.PHASE_COLORS[pid-1], 
			label=self.PHASE_NAMES[pid-1]) 
 			for pid in unique_phases]
		legend = self.ax.legend(
			handles=legend_elements, 
			title="Phases", 
			loc="center left", 
			bbox_to_anchor=(1, 0, 0.5, 1),
			prop={'size': 9},
			facecolor='#A0E0DD',
			edgecolor='#1E2E34')
		legend.get_title().set_fontsize(11)
		legend.get_title().set_weight('bold')

		self.draw()

	def bars_projects_vs_average(self, average_data: list[tuple[int, int]], 
		data1: list[tuple[int, int, str]], 
		data2: Optional[list[tuple[int, int, str]]] = None,
		data3: Optional[list[tuple[int, int, str]]] = None) -> None:
		"""Method to compare up to 3 projects' phases to the average phase duration"""
		self.ax = self.fig.add_subplot(111)
		self.ax.clear()

		x1 = [data[0] for data in data1]
		y1 = [data[1] for data in data1]
		proj1_name = data1[0][2]

		if data2:
			x2 = [data[0] for data in data2]
			y2 = [data[1] for data in data2]
			proj2_name = data2[0][2]

		if data3:
			x3 = [data[0] for data in data3]
			y3 = [data[1] for data in data3]
			proj3_name = data3[0][2]

		all_phases = set(x1)
		if data2:
			all_phases.update(x2)
		if data3:
			all_phases.update(x3)

		all_phases = sorted(all_phases)

		avg_y = [data[1] for data in average_data if data[0] in all_phases]

		colors = self.PHASE_COLORS[:len(all_phases)]
		num_projects = 1
		if data2:
			num_projects += 1
		if data3:
			num_projects += 1

		width = .75 / (num_projects + 1)
		x_positions = range(1,len(all_phases)+1)

		phase_name = [self.PHASE_NAMES_SHORT[phase_id - 1] for phase_id in all_phases]
		bars = self.ax.bar(all_phases, avg_y, width, color=self.PHASE_COLORS[7])
		self.ax.bar_label(bars, label_type='edge', 
			color = '#A0E0DD', fontsize=6)
		bars2 = self.ax.bar([x-width for x in x1], y1, width, color=self.PHASE_COLORS[5])
		self.ax.bar_label(bars2, label_type='edge', 
			color = '#A0E0DD', fontsize=6)
		if data2:
			bars3 = self.ax.bar([x-2*width for x in x2], y2, width, color=self.PHASE_COLORS[3])
			self.ax.bar_label(bars3, label_type='edge', 
				color = '#A0E0DD', fontsize=6)
		if data3:
			bars4 = self.ax.bar([x-3*width for x in x3], y3, width, color=self.PHASE_COLORS[2])
			self.ax.bar_label(bars4, label_type='edge', 
				color = '#A0E0DD', fontsize=6)

		self.ax.set_facecolor('#2A3F45')  # Plot area
		self.ax.spines['bottom'].set_color('#4A6F75')
		self.ax.spines['left'].set_color('#4A6F75')
		self.ax.spines['top'].set_visible(False)
		self.ax.spines['right'].set_visible(False)

		self.ax.tick_params(axis='x', rotation=15, labelsize=8, colors='#89D5D2')
		self.ax.tick_params(axis='y', labelsize=8, colors='#89D5D2')

		self.ax.set_xticks(x_positions)
		self.ax.set_xticklabels(phase_name, ha='right')

		self.fig.suptitle("Project Phases vs Average", color='#89D5D2', fontsize=12, y=0.97)
		self.ax.set_ylabel('Total Hours', color='#89D5D2')

		proj_names = ["Phase Average", proj1_name]
		if data2: 
			proj_names.append(proj2_name)
		if data3:
			proj_names.append(proj3_name)
		legend = self.ax.legend(proj_names, title="Projects", facecolor='#A0E0DD', edgecolor='#1E2E34')
		legend.get_title().set_fontsize(12)
		legend.get_title().set_weight('bold')
