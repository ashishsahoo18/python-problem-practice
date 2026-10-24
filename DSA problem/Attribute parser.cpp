int main() {
    int n,q;
    cin>> n >> q;
    cin.ignore();
    
    map<string,string> attributes;
    vector<string> path;
    
    for(int i=0; i<n; i++){
        string line;
        getline(cin,line);
        
        if(line[1] == '/'){
            path.pop_back();
            continue;
        }
        
        line = line.substr(1, line.size()-2 );
        
        stringstream ss(line);
        
        string tag;
        ss>>tag;
        path.push_back(tag);
        
        string currentPath = "";
        
        for(size_t j=0; j<path.size(); j++){
            if(j>0){
                currentPath += ".";
            }
            currentPath += path[j];
        }
        
        string attribute, equal, value;
        
        while(ss>>attribute>>equal>>value){
            value = value.substr(1,value.size()-2);
            
            string key = currentPath + "~" + attribute;
            
            attributes[key] = value;
        }
    }  
    
    for(int i=0; i<q; i++){
        string query;
        getline(cin,query);
        
        if(attributes.find(query) != attributes.end()){
            cout<<attributes[query]<<endl;
        }
        else{
            cout<<"Not Found!"<<endl;
        }
    }
    return 0;
}