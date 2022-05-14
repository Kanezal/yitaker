from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from friends.models import Friends


from rest_framework.views import APIView
from rest_framework.response import Response

from user_profile.models import Profile


def base_ctx() -> dict:
    return {
        "nav": {

            "Мои друзья": {
                "link": "my_friends"
            },
            "Возможные друзья": {
                "link": "friends"
            },
        }
    }


def my_friends(request):
    ctx = base_ctx()
    profiles = list()
    for profile in Profile.objects.all().order_by('-rating'):
        if str(Friends.objects.filter(user1=request.user, user2=profile.id, user2_confirmation=True)) != "<QuerySet []>" or str(Friends.objects.filter(user2=request.user, user1=profile.id, user2_confirmation=True)) != "<QuerySet []>":
            profiles.append(profile)
    ctx['profiles'] = profiles
    return render(request, 'friends.html', ctx)


def friends(request):
    ctx = base_ctx()
    profiles = list()
    for profile in Profile.objects.all().order_by('-rating'):
        if str(Friends.objects.filter(user1=request.user, user2=profile.id, user2_confirmation=True)) == "<QuerySet []>" and str(Friends.objects.filter(user2=request.user, user1=profile.id, user2_confirmation=True)) == "<QuerySet []>":
            profiles.append(profile)
    ctx['profiles'] = profiles
    return render(request, 'friends.html', ctx)



def is_friends(user1, user2) -> bool:
    """Func return

    Args:
        user1 (bool): request user
        user2 (bool): second user

    Returns:
        bool: is user2 friend with user1
    """
    fr = list(Friends.objects.filter(
        user1=user1,
        user2=user2,
    )) + list(Friends.objects.filter(
        user1=user2,
        user2=user1
    ))

    return fr[0].user2_confirmation


def is_outgoing_request(user1, user2):
    try:
        is_friends(user1, user2)

        fr = list(Friends.objects.filter(
            user1=user1,
            user2=user2,
        ))

        if len(fr) != 0:
            return True

        return False
    except IndexError:
        raise IndexError


class AddFriend(APIView):
    def get(self, request, id):
        friends = Friends.objects.filter(
            user1=request.user,
            user2=User.objects.get(id=id)
        )

        if len(friends) == 0:
            friend_req = Friends(
                user1=request.user,
                user2=User.objects.get(id=id)
            )
            friend_req.save()
            return Response({
                "success": True,
                "is_friends": False,
            })

        return Response({
            "success": False,
            "is_friends": bool(friends[0].user2_confirmation)
        })


class IsFriend(APIView):
    def get(self, request, id):
        user1 = request.user
        user2 = User.objects.get(id=id)
        try:
            if is_friends(user1, user2):
                return Response({
                    "friendButtonContent": "Удалить из друзей",
                })
            elif is_outgoing_request(user1, user2):
                return Response({
                    "friendButtonContent": "Заявка отправленна",
                })
            else:
                return Response({
                    "friendButtonContent": "Ответ на заявку",
                })
        except IndexError:
            return Response({
                "friendButtonContent": "Добавить в друзья"
            })


class AcceptFriend(APIView):
    def get(self, request, id):
        fr_req = Friends.objects.get(
            user1=User.objects.get(id=id),
            user2=request.user
        )
        fr_req.user2_confirmation = True
        fr_req.save()
        return Response({
            "success": True
        })


class DeleteFriend(APIView):
    def get(self, request, id):
        user1 = request.user
        user2 = User.objects.get(id=id)

        try:
            Friends.objects.get(user1=user1, user2=user2).delete()
        except Exception:
            Friends.objects.get(user1=user2, user2=user1).delete()
        
        return Response({
            "success": True
        })
