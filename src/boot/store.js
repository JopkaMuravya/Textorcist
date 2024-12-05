import  { boot } from 'quasar/wrappers';
import store from '../store.js';

export  default boot(({ app }) => {
    app.use(store);
});