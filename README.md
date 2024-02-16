# Doc2Vec IRS (News Document Indexing and Retrieval System)

Doc2Vec IRS is a document retrieval system that utilizes Doc2Vec embeddings for indexing and retrieving news documents. This system allows users to enter queries and target categories, and it returns relevant documents based on similarity scores calculated using Doc2Vec embeddings. Additionally, it provides precision and recall metrics for evaluating the retrieval results.

## Features

- **Document Retrieval:** Users can enter free-form queries along with target categories to retrieve relevant news documents.
- **Precision and Recall Calculation:** The system calculates precision and recall metrics to evaluate the retrieval performance.
- **Document Viewing:** Users can view the content of retrieved documents directly from the application.

## Installation

To set up and run the application, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/fenil210/Doc2VecIRS-News-Document-Indexing-and-Retrieval-System
    cd Doc2VecIRS-News-Document-Indexing-and-Retrieval-System
     ```

📦 APP
┣ 📜 app.py
┣ 📂 modules
┃ ┣ 📜 data_loader.py
┃ ┣ 📜 doc2vec_trainer.py
┃ ┗ 📜 query_handler.py
┣ 📂 templates
┃ ┣ 📜 index.html
┃ ┗ 📜 view_document.html


2. **Create and Activate Virtual Environment:**
    ```bash
    virtualenv venv
    # For Windows:
    venv\Scripts\activate
    # For Unix/macOS:
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```
    pip install Flask gensim pandas numpy scikit-learn numpy 
    ```

4. **Run the Application:**
    ```bash
    python -m flask --app .\app.py run
    ```

5. **Access the Application:**
    Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

### Index Page

- Enter your query, target category, and value of `k` in the provided form.
- Submit the form to retrieve relevant documents and view precision and recall metrics.

### Document View

- Click on any document link to view its content.

## Project Structure

- `app.py`: Main Flask application file containing routes and logic for handling user requests.
- `modules/`:
  - `data_loader.py`: Module for loading and preprocessing data from news documents.
  - `doc2vec_trainer.py`: Module for training the Doc2Vec model using Gensim.
  - `query_handler.py`: Module for processing user queries and retrieving relevant documents.
- `static/`: Directory containing static files such as CSS and JavaScript.
- `templates/`: Directory containing HTML templates for rendering web pages.

## Dependencies

- Flask: Web framework for building the application.
- Gensim: Library for training and using the Doc2Vec model.
- Pandas: Library for data manipulation and analysis.
- NumPy: Library for numerical computing.
- scikit-learn: Library for machine learning algorithms and tools.

## below is sample input 
![input website](https://github.com/fenil210/Doc2VecIRS-News-Document-Indexing-and-Retrieval-System/assets/121050723/ced8e596-262a-46b8-87fa-2955b6b0ac55)

## below is sample output
![output flask website](https://github.com/fenil210/Doc2VecIRS-News-Document-Indexing-and-Retrieval-System/assets/121050723/62883196-7665-4e8f-b885-6aa9b18090b0)

## Contributors

- [Your Name](https://github.com/fenil210)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
