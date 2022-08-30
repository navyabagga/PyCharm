int
main()
{
    int
n;
cin >> n;
vector < vector < int >> a(n - 1);
for (int i=0;i < n-1;i++)
{
    int
a1, a2;
cin >> a1 >> a2;
a[a1].push_back(a2);
}
int
k;
cin >> k;
unordered_set < int > s;
for (int i=0;i < k;i++)
{
    int
c;
cin >> c;
s.insert(c);
}
queue < int > q;
q.push(1);
int
mx = 0;
while (!q.empty())
{
    int
x = q.front();
q.pop();
for (auto i:a[x])
{
if (s.find(i) == s.end() & & s.find(x) == s.end())
{
    q.push(i);
mx + +;
}
}
}
cout << mx << endl;

return 0;
}