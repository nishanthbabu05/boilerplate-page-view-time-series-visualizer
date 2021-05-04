import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates = ["date"], index_col = "date")

# Clean data
df = df.loc[(df['value']>=df['value'].quantile(0.025))&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (10,5))
    ax=df['value'].plot(figsize=(20,5),color='red')
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    df_bar = df.copy()    
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['Months'] = [d.strftime('%B') for d in df_bar.date]
    df_bar=df_bar.drop(['date' ], axis = 1)
    df_bar=df_bar.groupby(['year','Months'],as_index=False).mean()



    df_bar=pd.pivot_table(df_bar, values='value', index=['year'],columns=['Months'])
    first_column = df_bar.pop('December')
    df_bar.insert(0, 'December', first_column)
    first_column = df_bar.pop('November')
    df_bar.insert(0, 'November', first_column)
    first_column = df_bar.pop('October')
    df_bar.insert(0, 'October', first_column)
    first_column = df_bar.pop('September')
    df_bar.insert(0, 'September', first_column)
    first_column = df_bar.pop('August')
    df_bar.insert(0, 'August', first_column)
    first_column = df_bar.pop('July')
    df_bar.insert(0, 'July', first_column)
    first_column = df_bar.pop('June')
    df_bar.insert(0, 'June', first_column)
    first_column = df_bar.pop('May')
    df_bar.insert(0, 'May', first_column)
    first_column = df_bar.pop('April')
    df_bar.insert(0, 'April', first_column)
    first_column = df_bar.pop('March')
    df_bar.insert(0, 'March', first_column)
    first_column = df_bar.pop('February')
    df_bar.insert(0, 'February', first_column)
    first_column = df_bar.pop('January')
    df_bar.insert(0, 'January', first_column)


    

    # Draw bar plot
       
    fig=df_bar.plot.bar(figsize=(10,10),xlabel="Years",ylabel="Average Page Views").get_figure()
    

    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, x = plt.subplots( ncols=2, figsize = (20,10))


    x[0] = sns.boxplot(x=df_box["year"], y=df_box["value"], ax = x[0])
    x[1] = sns.boxplot(x=df_box["month"], y=df_box["value"], ax = x[1],order=['Jan','Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    x[0].set_title("Year-wise Box Plot (Trend)")
    x[0].set_xlabel('Year')
    x[0].set_ylabel('Page Views')

    x[1].set_title("Month-wise Box Plot (Seasonality)")
    x[1].set_xlabel('Month')
    x[1].set_ylabel('Page Views')
    





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
