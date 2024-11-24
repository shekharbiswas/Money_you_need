import plotly.graph_objects as go

def swp_calculator_with_chart(initial_corpus, initial_withdrawal, years, inflation_rate=6):
    """
    Calculate and plot the SWP with inflation-adjusted withdrawals.

    :param initial_corpus: The starting corpus amount.
    :param initial_withdrawal: The initial withdrawal amount.
    :param years: Number of years withdrawals will be made.
    :param inflation_rate: Annual inflation rate (default: 6%).
    """
    inflation_rate /= 100  # Convert to decimal
    withdrawal = initial_withdrawal
    corpus = initial_corpus

    year_list = []
    withdrawal_list = []
    corpus_list = []

    for year in range(1, years + 1):
        # Adjust withdrawal for inflation
        if year > 1:
            withdrawal *= (1 + inflation_rate)

        # Record values for plotting
        year_list.append(year)
        withdrawal_list.append(withdrawal)
        corpus_list.append(corpus)

        # Deduct withdrawal from corpus
        corpus -= withdrawal

        # Stop if corpus is exhausted
        if corpus < 0:
            corpus_list.append(0)  # Corpus becomes zero after exhaustion
            print(f"Corpus exhausted in year {year}.")
            break

    # Create the Plotly chart
    fig = go.Figure()

    # Add corpus balance line
    fig.add_trace(go.Scatter(
        x=year_list, y=corpus_list, 
        mode='lines+markers', name='Remaining Corpus',
        line=dict(color='blue')
    ))

    # Add withdrawal line
    fig.add_trace(go.Scatter(
        x=year_list, y=withdrawal_list, 
        mode='lines+markers', name='Withdrawal Amount',
        line=dict(color='red')
    ))

    # Customize layout
    fig.update_layout(
        title="Systematic Withdrawal Plan (SWP) with Inflation Adjustment",
        xaxis_title="Year",
        yaxis_title="Amount",
        legend_title="Legend",
        template="plotly_white"
    )

    # Show the chart
    fig.show()

    return corpus_list[-1] if corpus_list else 0

# Example Usage
initial_corpus = 1000000  # Initial corpus (e.g., $1,000,000)
initial_withdrawal = 50000  # Initial annual withdrawal (e.g., $50,000)
years = 20  # Number of years for withdrawals

swp_calculator_with_chart(initial_corpus, initial_withdrawal, years)
