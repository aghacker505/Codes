int pop(){
    if(s.top==0)
    {
        printf("underflow");
        return;
    }

    int item = s.stack[s.top];
    s.top =s.top-1;
    return item;
}