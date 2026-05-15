import { initializeApp } from 'firebase/app';
import { getDatabase } from 'firebase/database';

const firebaseConfig = {
  apiKey: "AIzaSyDTGp-CAQmfuhuc4bGYXEaWoEhXnWMpPrU",
  authDomain: "smart-street-light-iot.firebaseapp.com",
  databaseURL: "https://smart-street-light-iot-default-rtdb.firebaseio.com",
  projectId: "smart-street-light-iot",
  storageBucket: "smart-street-light-iot.firebasestorage.app",
  messagingSenderId: "172628440766",
  appId: "1:172628440766:web:1226eac199f743273750ef"
};

const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);
