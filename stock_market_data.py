from pandas_datareader import data
from bokeh.plotting import figure, show, output_file
import datetime


start = datetime.datetime(2017,11,1)
end = datetime.datetime(2017,12,31)

df = data.DataReader(name='GOOG', data_source='google', start=start, end=end)


def inc_dec(c,o):
    if c > o:
        return 'Increase'
    elif c < o:
        return 'Decrease'
    else:
        return 'Equal'
    
df['Status'] = [inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
df['Middle'] = (df.Open + df.Close)/2
df['Height'] = abs(df.Open - df.Close)



p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode='scale_width')
p.title.text='Google stocks Nov 1, 2017 - Dec 31, 2017'
p.title.text_font_size = '20pt'
p.grid.grid_line_alpha = 0.3

hours_12 = 10*60*60*1000



p.segment(df.index, df.High, df.index, df.Low, color='black')

p.rect(df.index[df.Status == 'Increase'], df.Middle[df.Status == 'Increase'], hours_12,
       df.Height[df.Status == 'Increase'], fill_color='#f0f0f0', line_color='black')

p.rect(df.index[df.Status == 'Decrease'], df.Middle[df.Status == 'Decrease'], hours_12,
       df.Height[df.Status == 'Decrease'], fill_color='#ff0000', line_color='black')



output_file('Candlestick_Graph.html')
show(p)