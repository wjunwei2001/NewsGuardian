import React, { useState } from 'react';
import './NewsGuardian.css';

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
            <p className='header'>NewsGuardian</p>
            <p style={{ textAlign: 'center' }}>Verify article authenticity <strong>instantly</strong> with our fake news detector. <br></br>Paste the text into the textbox below and click <strong>"Predict"</strong> for accurate results.</p>
            <form onSubmit={handleSubmit}>
                <textarea className='textbox' type="text" id="userinput" name="text" placeholder="Enter your text here..." value={text} onChange={handleInputChange} cols={60} />
                <br />
                <br />
                <button className='submitbutton' type="submit" name="predict">Predict</button>
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