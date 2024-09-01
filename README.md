<h1>Olympic Data Analysis</h1>
[https://ku-sh-24-olympic-data-project-olympic-analysis-v1zr6v.streamlit.app/](url)
<p>This project utilizes 120 years of Olympic history data, focusing on athletes and their results. The analysis is conducted using Jupyter Notebook and presented via a web application created with Streamlit in PyCharm.</p>

<h2>Libraries Used</h2>
<ul>
  <li>Streamlit</li>
  <li>Pandas</li>
</ul>

<h2>Basic Framework</h2>
<p>The analysis is structured around the following main sections:</p>
<ol>
  <li><strong>Medal Tally</strong></li>
  <li><strong>Overall Analysis</strong></li>
  <li><strong>Country-wise Analysis</strong></li>
  <li><strong>Athlete-wise Analysis</strong></li>
</ol>

<h2>Data Overview</h2>
<ul>
  <li><strong>Time Window:</strong> The data spans from 1896 to 2016, encompassing almost 120 years of Olympic history.</li>
  <li><strong>Datasets:</strong> Two datasets are available:
    <ul>
      <li>Dataset containing information about athletes and their performances.</li>
      <li>Dataset containing the full names of country abbreviations.</li>
    </ul>
  </li>
</ul>

<h2>Data Preprocessing</h2>
<ul>
  <li><strong>Handling Historical Changes:</strong> Some countries did not exist in the past, and some underwent name changes. Special attention was given to researching and addressing these cases.</li>
  <li><strong>One-Hot Encoding:</strong> Medals were encoded using one-hot encoding for analysis purposes.</li>
</ul>

<h2>Usage</h2>
<p>To run the analysis:</p>
<ol>
  <li>Clone this repository.</li>
  <li>Ensure you have the necessary libraries installed (<code>streamlit</code>, <code>pandas</code>, etc.).</li>
  <li>Run the Streamlit app in PyCharm or any other Python environment.</li>
</ol>

<h2>Major Issues and Solutions</h2>
<p>Major issues occurred with ranking the nations since the data was organized athlete-wise. The team sports medals were being counted multiple times, resulting in duplicates in the medal tally. To address this, duplicates with the same team, NOC region, etc., were dropped.</p>
<p>Functions were created in PyCharm to show the analysis and present it using Streamlit methods. Different conditions were implemented based on the choices made in the radio buttons to enhance user interaction. Continuous validation was performed with specific cases to ensure the code accurately reflected the data available on the internet.</p>

<h2>Additional Notes</h2>
<ul>
  <li>The analysis aims to provide insights into Olympic data spanning over a century, covering various aspects such as medal distribution, historical trends, and individual athlete performances.</li>
</ul>

<h2>Usage</h2>
<p>To run the analysis:</p>
<ol>
  <li>Clone this repository.</li>
  <li>Ensure you have the necessary libraries installed (<code>streamlit</code>, <code>pandas</code>, etc.).</li>
  <li>Run the Streamlit app in PyCharm or any other Python environment.</li>
</ol>

<h2>Major Issues and Solutions</h2>
<p>Major issues occurred with ranking the nations since the data was organized athlete-wise. The team sports medals were being counted multiple times, resulting in duplicates in the medal tally. To address this, duplicates with the same team, NOC region, etc., were dropped.</p>
<p>Functions were created in PyCharm to show the analysis and present it using Streamlit methods. Different conditions were implemented based on the choices made in the radio buttons to enhance user interaction. Continuous validation was performed with specific cases to ensure the code accurately reflected the data available on the internet.</p>

<h2>Additional Notes</h2>
<ul>
  <li>The analysis aims to provide insights into Olympic data spanning over a century, covering various aspects such as medal distribution, historical trends, and individual athlete performances.</li>
</ul>
