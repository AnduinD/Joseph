from json import dumps
from random import randint
# ����һ�����ӻ����ݽṹ
graph = {
    "kind": {"graph": True},
    "nodes": [

    ],
    "edges": []
}
# Ϊ�˷�����ʾ���Ҽ����㷨����ȷ��,��Ϊ��num���õ�СһЩ
num = 25
# ����һ��ѭ������
for i in range(1,num):
    j = randint(-20,20)
    # �����µĽڵ�
    graph['nodes'].append({'id':str(i),'code':j})
    # �������ӹ�ϵ
    graph['edges'].append({'from':str(i),'to':str(i+1),'label':str(j)})
    # ���Ϊjson��ʽ������ӻ�
    json_graph = dumps(graph)
# �ֶ������һ��Ԫ�غ���ʼԪ����������
graph['edges'][num-2]['to'] = '1'
# ��ʾ���ս��
json_graph = dumps(graph)

# ��ʼ��ʽ��Լɪ��
# ���´�����ֲ�����JosephByList����,ֻ�����һЩ���ӻ�tips

# �������һ����ʼ����
index = 5
while len(graph['nodes']) > 0:
    # �ýڵ��ǰһ���ڵ�ָ����һ��
    graph['edges'][(index-1)%len(graph['nodes'])]['to'] = graph['edges'][index]['to']
    # ���ӻ�
    json_graph = dumps(graph)
    # ɾ���ڵ�
    subdict = graph['nodes'].pop(index)
    # ɾ�����ӹ�ϵ
    graph['edges'].pop(index)
    # ���ӻ�
    json_graph = dumps(graph)
    
    # ��ӡ��������Ҫ����Ϣ
    print(subdict['id'])

    # ������Ѱ����һ����Ҫ�����Ķ���
    # �����Ϊ�˱������Ϊ0�����
    if len(graph['nodes']) > 0:
        if subdict['code']>0:
            # ���code��ֵ����0��ô�µ��±꼴Ϊ��ԭ���Ļ����ϼӶ�Ӧ��code��ȥһ(��Ϊ��Ԫ���Ѿ���ɾ������)�����ܳ���
            index = (index + subdict['code']-1)%len(graph['nodes'])
        else:
            # ���code��ֵС��0��ô�൱�ڴ�ǰ�����������Ǵ�ǰ��������ʱ������ڵ���±�û��Ӱ�����Բ���Ҫ��һ
            index = (index+subdict['code'])%len(graph['nodes'])
    else:
        index = 0

graph['edges'].pop(0)
graph['nodes'].pop(0)
print("Finished")


