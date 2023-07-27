document.getElementById('submitBtn').addEventListener('click', function() {
  const networkDataset = document.getElementById('networkDataset').value;
  const codeGadgetDataset = document.getElementById('codeGadgetDataset').value;

  // Check if both datasets are selected
  if (networkDataset && codeGadgetDataset) {
    // Prepare the data to send in the API request
    const formData = new FormData();
    formData.append('network_traffic_dataset', networkDataset);
    formData.append('source_code_samples_dataset', codeGadgetDataset);

    // Call your backend API here to send the selected datasets and receive the output
    fetch('/predict', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        // Update the outputContainer div with the results
        const outputContainer = document.getElementById('outputContainer');
        outputContainer.innerHTML = `
          <h2>Output:</h2>
          <p>${data.result}</p>
        `;
      })
      .catch(error => {
        console.error('Error:', error);
        // Display error message if something goes wrong
        const outputContainer = document.getElementById('outputContainer');
        outputContainer.innerHTML = `
          <h2>Output:</h2>
          <p>Error occurred while processing the request.</p>
        `;
      });
  } else {
    alert('Please select both Network Traffic Dataset and Code Gadget Dataset.');
  }
});
