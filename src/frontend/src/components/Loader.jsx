import React from "react";
import { Box, CircularProgress, Typography } from "@mui/material";

const Loader = ({ message = "Chargement..." }) => {
  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      height="100vh"
      flexDirection="column"
    >
      <CircularProgress />
      {message && (
        <Typography variant="body2" style={{ marginTop: "10px", color: "#555" }}>
          {message}
        </Typography>
      )}
    </Box>
  );
};

export default Loader;
