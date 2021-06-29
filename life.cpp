#include <iostream>
#include <set>
using namespace std;
#define nl '\n'

set<pair<int,int> > s, nextgen;

int cnt(pair<int,int>);
void finish();

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	freopen("comms.txt","r",stdin);
	// freopen("seed.txt","r",stdin);
	int in1, in2;
	while(cin >> in1){
		cin >> in2;
		s.insert({in1, in2});
	}
	
	int x, y, n;
	for(set<pair<int,int> >::iterator it=s.begin(); it!=s.end(); it++){
		for(x=-1; x<2; x++) for(y=-1; y<2; y++){
			n=cnt({it->first+x, it->second+y});
			if(n==3){
				nextgen.insert({it->first+x, it->second+y});
			}
			else if(n==4){
				if(s.find({it->first+x, it->second+y}) != s.end())
					nextgen.insert({it->first+x, it->second+y});
			}
		}
	}
	
	finish();
}

int cnt(pair<int,int> p){
	int ret=0, x=p.first, y=p.second;
	set<pair<int,int> >::iterator it;
	it=s.lower_bound({x-1,y-1});
	while(it!= s.end() && it->first == x-1 && it->second <= y+1){
		it++;
		ret++;
	}
	it=s.lower_bound({x,y-1});
	while(it!= s.end() && it->first == x && it->second <= y+1){
		ret++;
		it++;
	}
	it=s.lower_bound({x+1,y-1});
	while(it!= s.end() && it->first == x+1 && it->second <= y+1){
		ret++;
		it++;
	}
	return ret;
}

void finish(){
	freopen("comms.txt","w",stdout);
	for(set<pair<int,int> >::iterator it=nextgen.begin(); it!=nextgen.end(); it++){
		cout << it->first << ' ' << it->second << ' ';
	}
}
