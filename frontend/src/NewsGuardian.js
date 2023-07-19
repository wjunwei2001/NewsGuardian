import React, { useState } from 'react';

function NewsGuardian() {
    const [text, setText] = useState('')
    const [result,setResult] = useState('');
    
    const handleInputChange = (element) => { 
      setText(element.target.value);

      if (element) {
      const target = element.target ? element.target : element; 
      element.target.style.height = 'auto';
      element.target.style.height = `${target.scrollHeight}px`;
    }
  };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('/predict/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text }),
        });
        const data = await response.json();
        setResult(data.result);
      };

    return (
        <div style={{ textAlign: 'center' }}>
            <h1 style={{ textAlign: 'center' }} >NewsGuardian Fake News Detector</h1>
            <p style={{ textAlign: 'center' }}>Verify your information here</p>
            <form onSubmit={handleSubmit}>
                <textarea type="text" id="userinput" name="text" placeholder="Enter your text here..." value={text} onChange={handleInputChange} cols={60} />
                <br />
                <button type="submit" name="predict">Predict</button>
            </form>
            {result && (
                <p style={{ textAlign: 'center' }}>
                <strong>Prediction: {result}</strong>
                </p>
            )}
        </div>
    );
}

export default NewsGuardian;