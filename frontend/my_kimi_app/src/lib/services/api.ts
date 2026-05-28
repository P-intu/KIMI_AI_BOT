import axios from "axios";

 export async function promptGeminiai(data:{message:string}){
    try {
        const response = await axios.post("http://127.0.0.1:8000/ai/chat_with_kimihelp/", data);
        return response.data;
    } catch (error) {
       if (axios.isAxiosError(error)){
        throw new Error(error.response?.data.error || error.message)
       }
}
}