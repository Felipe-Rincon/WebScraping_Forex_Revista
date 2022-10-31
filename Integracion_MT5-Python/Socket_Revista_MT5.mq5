//+------------------------------------------------------------------+
//|                                           Socket_Revista_MT5.mq5 |
//|                                  Copyright 2022, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
sinput int lrlenght = 1;
int socket;

//---------------- El socket envia------------------

bool socksend(int sock,string request) 
  {
   char req[];
   int  len=StringToCharArray(request,req)-1;
   if(len<0) return(false);
   return(SocketSend(sock,req,len)==len); 
  }
  
 //---------------------------------------------------
 
 //---------------Leyendo la respuestas---------------
 
 string socketreceive(int sock,int timeout)
  {
   char rsp[];
   string result="";
   uint len;
   uint timeout_check=GetTickCount()+timeout;
   
   do
     {
      len=SocketIsReadable(sock);
      if(len)
        {
         int rsp_len;
         rsp_len=SocketRead(sock,rsp,len,timeout);
         if(rsp_len>0) 
           {
            result+=CharArrayToString(rsp,0,rsp_len); 
           }
        }
     }
   while((GetTickCount()<timeout_check) && !IsStopped());
   return result;
  }
 
//---------------------------------------------------

//-----------------Visualizamos----------------------

void drawlr(string points) {
   string res[];
   StringSplit(points,' ',res);

   if(ArraySize(res)==4) 
     {
      Print(StringToDouble(res[0]));
      Print(StringToDouble(res[1]));
      Print(StringToDouble(res[2]));
      Print(StringToDouble(res[3]));
      datetime temp[];
      CopyTime(Symbol(),Period(),TimeCurrent(),lrlenght,temp);
      
      ObjectCreate(0,"Z_1",OBJ_HLINE,0,0,NormalizeDouble(StringToDouble(res[0]),_Digits));
      ObjectCreate(0,"Z_2",OBJ_HLINE,0,0,NormalizeDouble(StringToDouble(res[1]),_Digits));
      ObjectCreate(0,"Z_3",OBJ_HLINE,0,0,NormalizeDouble(StringToDouble(res[2]),_Digits));
      ObjectCreate(0,"Z_4",OBJ_HLINE,0,0,NormalizeDouble(StringToDouble(res[3]),_Digits));
      
      
     
     }
    }
    
//---------------------------------------------------

//----------------------Info que se envia -----------
  
void OnTick() {
 socket=SocketCreate();
 if(socket!=INVALID_HANDLE) {
  if(SocketConnect(socket,"127.0.0.1",9090,1000)) {
   Print("Connected to ","127.0.0.1",":",9090);
         
   double clpr[];
   int copyed = CopyClose(_Symbol,PERIOD_CURRENT,0,lrlenght,clpr);
         
   string tosend;
   for(int i=0;i<ArraySize(clpr);i++) tosend+=(string)clpr[i]+" ";       
   string received = socksend(socket, tosend) ? socketreceive(socket, 10) : ""; 
   drawlr(received); }
   
  else Print("Connection ","127.0.0.1",":",9090," error ",GetLastError());
  SocketClose(socket); }
 else Print("Socket creation error ",GetLastError()); }
 
//---------------------------------------------------
