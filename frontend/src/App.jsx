import React, { useState, useEffect } from 'react';
import { Container, Typography, Box, CircularProgress, Grid } from '@mui/material';
import axios from 'axios';

// Function to get month name from index
const getMonthName = (index) => {
    const baseDate = new Date();  // Use current date to find month
    baseDate.setMonth(baseDate.getMonth() + index);  // Add index to current month
    return baseDate.toLocaleString('default', { month: 'long', year: 'numeric' });  // Get month and year
};

const App = () => {
    const [predictions, setPredictions] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Fetch predictions from the backend
        axios.get('/api/predict')
            .then((response) => {
                setPredictions(response.data);
                setLoading(false);
            })
            .catch((error) => {
                console.error("There was an error fetching the data!", error);
            });
    }, []);

    if (loading) {
        return <CircularProgress />;
    }

    return (
        <Container>
            <Typography variant="h4" align="center" gutterBottom>
                Revenue Predictions for Next 12 Months
            </Typography>
            <Box mt={4}>
                <Grid container spacing={3}>
                    {predictions.map((revenue, index) => (
                        <Grid item xs={12} sm={6} md={3} key={index}>
                            <Box p={2} border={1} borderColor="grey.300">
                                <Typography variant="h6" align="center">
                                    {getMonthName(index)}
                                </Typography>
                                <Typography variant="body1" align="center">
                                    Revenue: ${revenue.toFixed(2)}
                                </Typography>
                            </Box>
                        </Grid>
                    ))}
                </Grid>
            </Box>
        </Container>
    );
};

export default App;
