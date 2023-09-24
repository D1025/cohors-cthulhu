import React from 'react';
import {BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';
import Wrapper from './PlaySheet/Wrapper';
import Creation from './CreationSheet/Creation';

class App extends React.Component {
    render() {
        return (
            <div>
                <Router>
                <Routes>
                    <Route path="/"  element={<Wrapper />} />
                    <Route path="/create" element={<Creation />} />

                    {/* Catch-all route for invalid routes */}
                    <Route path="*" element={<Navigate to="/" />} />

                </Routes>
                </Router>
            </div>
        );
    }
}

export default App;