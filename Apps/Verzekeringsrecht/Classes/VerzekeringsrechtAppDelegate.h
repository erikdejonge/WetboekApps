//
//  VerzekeringsrechtAppDelegate.h
//  Verzekeringsrecht
//
//  Created by rabshakeh on 3/1/10 - 4:25 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class VerzekeringsrechtViewController;

@interface VerzekeringsrechtAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    VerzekeringsrechtViewController *viewController;
    UINavigationController    *navigationController ;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet VerzekeringsrechtViewController *viewController;

@end

