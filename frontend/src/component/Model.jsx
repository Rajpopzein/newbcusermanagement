import Modal from '@mui/material/Modal';
import React from 'react'
import { Box } from '@mui/material';


const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  // width: 400,
  bgcolor: 'background.paper',
  // border: '2px solid #000',
  boxShadow: 24,
  p: 4,
  borderRadius:'1rem'
};

const ModelPoper = ({open, handleClose, children}) => {
  return (
    <Modal
    open={open}
    onClose={handleClose}
    aria-labelledby="modal-modal-title"
    aria-describedby="modal-modal-description"
  >
    <Box sx={style}>
     {children}
    </Box>
  </Modal>
  )
}

export default ModelPoper